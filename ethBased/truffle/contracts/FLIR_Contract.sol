// SPDX-License-Identifier: MIT


pragma solidity >=0.4.4;

// library for logging in console
// import "hardhat/console.sol";


contract FLIRContract{

    uint btp = 3;

    uint btc1 = 3;
    uint btc2 = 4;
    uint btc3 = 5;
    uint btc4 = 6;
    uint btc5 = 7;
    uint btc6 = 8;
    uint btc7 = 9;
    uint btc8 = 10;

    function getnPnCnEV(uint nPget, uint nCget,uint nEVget) public 
    returns (uint,uint,uint)
    {
        
       uint nP = nPget;
       uint nC = nCget;
       uint nEV = nEVget;
       return (nP,nC,nEV);
    }

    function getProsumerTariff(uint Pexp) public 
    returns (uint)
    {
       uint Tp = Pexp * btp;
       return (Tp);
    }

    function getConsumerTariff(uint Cimp) public 
    returns (uint)
    {
        uint Tc = 0;
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

    function sendViaTransfer(address payable _to) public
    payable
    {
    _to.transfer(msg.value);
    }

    function prosumerReward(uint P1, uint delta) public
    returns (uint)
    {
        uint reward = (P1 * btp) + (delta * btp) + (delta * delta * btp / (delta+P1));
        return(reward);
    }

}