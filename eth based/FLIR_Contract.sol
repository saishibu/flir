pragma solidity ^0.4.4;

// library for logging in console
import "hardhat/console.sol";


contract FLIRContract{
    uint nP = 5;
    uint nC = 3;

    uint btp = 3;

    uint btc1 = 3;
    uint btc2 = 4;
    uint btc3 = 5;
    uint btc4 = 6;
    uint btc5 = 7;
    uint btc6 = 8;
    uint btc7 = 9;
    uint btc8 = 10;

    uint cost1 = 0;
    uint cost2 = 0;
    uint tCost = 0;
    // constructor() {}

    function ConsumerSlabPrice1(uint Cimp1)public view returns (uint cost1, string memory){
        cost1 = Cimp1 * btc1;
        return (cost1, integerToString(cost1));
    }

    function ConsumerSlabPrice2(uint Cimp2)public view returns (string memory){
        cost2 = Cimp2 * btc1;
        return integerToString(cost2);
    }

    function totalCost(uint cost1, uint cost2)public view returns (string memory){
        tCost = cost1 + cost2;
        return integerToString(tCost);

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