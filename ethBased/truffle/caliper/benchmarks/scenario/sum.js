'use strict';

const { WorkloadModuleBase } = require('@hyperledger/caliper-core');

class MyWorkload extends WorkloadModuleBase {
    constructor() {
        super();
    }

    async initializeWorkloadModule(workerIndex, totalWorkers, roundIndex, roundArguments, sutAdapter, sutContext) {
        await super.initializeWorkloadModule(workerIndex, totalWorkers, roundIndex, roundArguments, sutAdapter, sutContext);
        
        for(let i = 0; i < this.roundArguments.assets; i++){
            let request = {
                contract: 'simplecalc',
                readOnly: false,
                verb: 'sum',
                args: ["5", "6"]
            };  

            await this.sutAdapter.sendRequests(request);

        }
    }

    async submitTransaction() {
        for (let i = 0; i < this.roundArguments.assets; i++) {
            let request2 = {
                contract: 'simplecalc',
                readOnly: true,
                verb: 'sumout',
                args: []
            };

            await this.sutAdapter.sendRequests(request2);

        }
    }
}

function createWorkloadModule() {
    return new MyWorkload();
}

module.exports.createWorkloadModule = createWorkloadModule;