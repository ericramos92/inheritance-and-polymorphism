class BasicPlan{
    constructor(canStream,canDownload,hasSD,hasHD,hasUHD,numOfDevices,prices){
        this._canStream = canStream;
        this._canDownload = canDownload;
        this._hasSD = hasSD;
        this._hasHD = hasHD;
        this._hasUHD = hasUHD;
        this._numOfDevices = numOfDevices;
        this._prices = prices;
    }
    get canStream(){
        return this._canStream;
    }
    get canDownload(){
        return this._canDownload;
    }
    get hasSD(){
        return this._hasSD;
    }
    get hasHD(){
        return this._hasHD;
    }
    get hasUHD(){
        return this._hasUHD;
    }
    get numOfDevices(){
        return this._numOfDevices;
    }
    get prices(){
        return this._prices;
    }
}
//standard
class StandardPlan extends BasicPlan{
    constructor(canStream,canDownload,hasSD,hasHD,hasUHD,numOfDevices,prices){
        super(canStream,canDownload,hasSD,hasHD,hasUHD,numOfDevices,prices)
    }
}
// premium
class PremiumPlan extends BasicPlan{
    constructor(canStream,canDownload,hasSD,hasHD,hasUHD,numOfDevices,prices){
        super(canStream,canDownload,hasSD,hasHD,hasUHD,numOfDevices,prices)
    }
}

let planbasic = new BasicPlan(true,true,true,false,false,1,8.99);
let planstandard = new StandardPlan(true,true,true,true,false,2,12.99);
let planpremium = new PremiumPlan(true,true,true,true,false,4,15.99);

console.log(planbasic.hasSD);
console.log(planpremium.hasSD);
console.log(planbasic.hasUHD);
console.log(planbasic.prices);
console.log(planpremium.numOfDevices);