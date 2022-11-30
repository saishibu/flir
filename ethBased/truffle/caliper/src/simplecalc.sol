// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.4.22;



contract simplecalc {

    int public sum1;

    function sum(int a, int b) public returns(int){
        sum1 = a + b;
        return sum1;
    }

    function sumout() public view returns (int){
        return sum1;
    }
}
