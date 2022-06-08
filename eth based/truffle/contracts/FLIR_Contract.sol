pragma solidity ^0.4.4;

// library for logging in console
// import "hardhat/console.sol";


contract FLIRContract{
    mapping(address => uint256) private balaces;
    mapping(address => role) private roles;
    enum role{
        Prosumers,
        Consumers,
        Nanogrid,
        EV
    }


    // constructor() public{}

    uint public nP;
    uint public nC;
    uint public nEV;

    uint public btp = 3;

    uint public btc1 = 3;
    uint public btc2 = 4;
    uint public btc3 = 5;
    uint public btc4 = 6;
    uint public btc5 = 7;
    uint public btc6 = 8;
    uint public btc7 = 9;
    uint public btc8 = 10;

    

    function getnPnCnEV(uint nPget, uint nCget,uint nEVget) public{
        
        nP = nPget;
        nC = nCget;
        nEV = nEVget;
        console.log("NP = %s",nP);
        console.log("NC = %s",nC);
        console.log("NEV = %s",nEV);
        // return (nP1,nC1);
    }

    // function getProsumerTariff(uint nPget, uint nCget,uint nEVget) public{}

    // uint public amount = 1 ether;


    function send(address _addr, uint amount) payable public {
        require(msg.value >= amount);
        _addr.transfer(msg.value);
    }


//   uint public balance = 0;
  
//   function () payable {
//     balance += msg.value;
//   }


    
    

    function integerToString(uint _i) internal pure 
      returns (string memory) {
      
      if (_i == 0) {
         return "0";
      }
      uint j = _i;
      uint len;
      
      while (j != 0) {
         len++;
         j /= 10;
      }
      bytes memory bstr = new bytes(len);
      uint k = len - 1;
      
      while (_i != 0) {
         bstr[k--] = byte(uint8(48 + _i % 10));
         _i /= 10;
      }
      return string(bstr);//access local variable
   }



}