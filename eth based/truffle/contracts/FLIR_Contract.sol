// SPDX-License-Identifier: MIT


pragma solidity >=0.4.4;

// library for logging in console
// import "hardhat/console.sol";


contract FLIRContract{
    address public owner;
    address public manager;
    address[16] public seller;
    address[16] public buyers;

    // mapping(address => uint) public balances;
    // mapping(address => uint256) private balaces;
    // mapping(address => role) private roles;
    
    // // mapping(uint256 => address payable) Prosumers;
    // // mapping(uint256 => address payable) Consumers;
    // // mapping(uint256 => address payable) Nanogrid;
    // // mapping(uint256 => address payable) EV;
    
    // enum role{
    //     Prosumers,
    //     Consumers,
    //     Nanogrid,
    //     EV
    // }

    uint public balance = 0;
    // constructor() public{
    //     owner = msg.sender;
    // }

    // uint public nP;
    // uint public nC;
    // uint public nEV;

    uint public btp = 3;

    uint public btc1 = 3;
    uint public btc2 = 4;
    uint public btc3 = 5;
    uint public btc4 = 6;
    uint public btc5 = 7;
    uint public btc6 = 8;
    uint public btc7 = 9;
    uint public btc8 = 10;

    function sellerID(uint nPget) public returns (uint) {
        require (nPget >=0 && nPget <= 10);
        seller[nPget] = msg.sender;
        return nPget;
    }

    function getSellers() public view returns (address[16] memory){
        return seller;
    }
    

    function getnPnCnEV(uint nPget, uint nCget,uint nEVget) public
    returns (uint nP,uint nC,uint nEV){
        
        nP = nPget;
        nC = nCget;
        nEV = nEVget;
        // console.log("NP = %s",nP);
        // console.log("NC = %s",nC);
        // console.log("NEV = %s",nEV);
        return (nP,nC,nEV);
    }

    function getProsumerTariff(uint Pexp) public returns (uint Tp){
        Tp = Pexp * btp;
        return (Tp);
    }

    function getConsumerTariff(uint Cimp) public returns (uint Tc){
        
        if(Cimp < 251){
            if(Cimp < 51){
                Tc = Cimp * btc1;
            }
            else if(Cimp > 50 && Cimp < 101){
                Tc = (50 * btc1) + ((Cimp-50) * btc2);
            }
            else if(Cimp > 100 && Cimp < 151){
                Tc = (50 * btc1) + (50 * btc2) + ((Cimp-50) * btc3);
            }
            else if(Cimp > 150 && Cimp < 201){
                Tc = (50 * btc1) + (50 * btc2) + (50 * btc3) + ((Cimp-50) * btc4);
            }
            else if(Cimp > 200 && Cimp < 251){
                Tc = (50 * btc1) + (50 * btc2) + (50 * btc3) + (50 * btc4) + ((Cimp-50) * btc5);
            }
        }
        else if(Cimp > 250 && Cimp < 351){
            Tc = Cimp * btc6;
        }
        else if(Cimp > 350 && Cimp < 451){
            Tc = Cimp * btc7;
        }
        else if(Cimp > 450){
            Tc = Cimp * btc8;
        }
        return (Tc);
    }

    function send(address payable _receiver, uint amount) payable public {
    // _receiver.call.value(msg.value).gas(20317)();
        require(msg.value >= amount);
        _receiver.transfer(amount);
    }

    function balCheck() public payable {
    balance += msg.value;
    }

    function getBalance(address _balanceCheck) public returns (uint bal){
        bal = _balanceCheck.balance;
        return (bal);

    }


    // function getProsumerTariff(uint nPget, uint nCget,uint nEVget) public{}

    // uint public amount = 1 ether;


    // function send(address _addr, uint amount) payable public {
    //     require(msg.value >= amount);
    //     _addr.transfer(msg.value);
    // }


//   uint public balance = 0;
  
//   function () payable {
//     balance += msg.value;
//   }


    
    

//     function integerToString(uint _i) internal pure 
//       returns (string memory) {
      
//       if (_i == 0) {
//          return "0";
//       }
//       uint j = _i;
//       uint len;
      
//       while (j != 0) {
//          len++;
//          j /= 10;
//       }
//       bytes memory bstr = new bytes(len);
//       uint k = len - 1;
      
//       while (_i != 0) {
//          bstr[k--] = byte(uint8(48 + _i % 10));
//          _i /= 10;
//       }
//       return string(bstr);//access local variable
//    }



}

// contract Receiver {
//   uint public balance = 0;
  
//   function () payable {
//     balance += msg.value;
//   }
// }