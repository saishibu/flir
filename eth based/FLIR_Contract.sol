pragma solidity ^0.4.4;

// library for logging in console
import "hardhat/console.sol";


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

    uint nP;
    uint nC;
    uint nEV;

    // uint btp = 3;

    // uint btc1 = 3;
    // uint btc2 = 4;
    // uint btc3 = 5;
    // uint btc4 = 6;
    // uint btc5 = 7;
    // uint btc6 = 8;
    // uint btc7 = 9;
    // uint btc8 = 10;

    

    function getnPnCnEV(uint nPget, uint nCget,uint nEVget) public{
        
        nP = nPget;
        nC = nCget;
        nEV = nEVget;
        console.log("NP = %s",nP);
        console.log("NC = %s",nC);
        console.log("NEV = %s",nEV);
        // return (nP1,nC1);
    }



    
    

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