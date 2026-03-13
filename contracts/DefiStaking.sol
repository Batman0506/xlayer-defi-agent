// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title XLayer DeFi Staking Contract
 * @dev Staking contract for X Layer DeFi Agent
 */
contract XLayerStaking {
    
    // Token interfaces
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    
    // Staking state
    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public stakingTime;
    mapping(address => uint256) public rewards;
    
    // Configuration
    uint256 public rewardRate = 155; // 15.5% APY
    uint256 public constant SECONDS_PER_YEAR = 365 days;
    uint256 public totalStakers;
    
    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    
    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }
    
    // Stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");
        
        if (stakingBalance[msg.sender] == 0) {
            totalStakers++;
        }
        
        stakingBalance[msg.sender] += _amount;
        stakingTime[msg.sender] = block.timestamp;
        
        stakingToken.transferFrom(msg.sender, address(this), _amount);
        
        emit Staked(msg.sender, _amount);
    }
    
    // Unstake tokens
    function unstake(uint256 _amount) external {
        require(stakingBalance[msg.sender] >= _amount, "Insufficient balance");
        
        // Calculate rewards
        uint256 reward = calculateReward(msg.sender);
        rewards[msg.sender] += reward;
        
        stakingBalance[msg.sender] -= _amount;
        
        if (stakingBalance[msg.sender] == 0) {
            totalStakers--;
        }
        
        stakingToken.transfer(msg.sender, _amount);
        
        emit Unstaked(msg.sender, _amount);
    }
    
    // Claim rewards
    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    // Calculate pending rewards
    function calculateReward(address _user) public view returns (uint256) {
        if (stakingBalance[_user] == 0) return 0;
        
        uint256 timeStaked = block.timestamp - stakingTime[_user];
        uint256 rate = (rewardRate * stakingBalance[_user] * timeStaked) / SECONDS_PER_YEAR / 100;
        
        return rate;
    }
    
    // Get stake info
    function getStakeInfo(address _user) external view returns (
        uint256 balance,
        uint256 stakedTime,
        uint256 pendingReward
    ) {
        return (
            stakingBalance[_user],
            stakingTime[_user],
            calculateReward(_user)
        );
    }
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
