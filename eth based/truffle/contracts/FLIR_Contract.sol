// SPDX-License-Identifier: MIT


pragma solidity >=0.4.4;

// library for logging in console
// import "hardhat/console.sol";


contract FLIRContract{

    uint public btp = 3;

    uint public btc1 = 3;
    uint public btc2 = 4;
    uint public btc3 = 5;
    uint public btc4 = 6;
    uint public btc5 = 7;
    uint public btc6 = 8;
    uint public btc7 = 9;
    uint public btc8 = 10;

    function getnPnCnEV(uint nPget, uint nCget,uint nEVget) public pure
    returns (uint nP,uint nC,uint nEV){
        
        nP = nPget;
        nC = nCget;
        nEV = nEVget;
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

    function sendViaTransfer(address payable _to) public payable{
    _to.transfer(msg.value);
    }

}