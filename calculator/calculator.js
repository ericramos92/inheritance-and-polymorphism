class calculator{
    constructor(num1,num2){
        this._num1 = num1;
        this._num2 = num2;
    }
    get num1(){
        return this._num1;
    }
    get num2(){
        return this._num2;
    }
    add(){
        return this._num1 + this._num2;
    }
    subtract(){
        return this._num1 - this._num2;
    }
    multiply(){
        return this._num1 * this._num2;
    }
    devide(){
        return this._num1 / this._num2;
    }
    
}

const answer = new calculator(10,5);
console.log(answer.add())
console.log(answer.subtract())
console.log(answer.multiply())
console.log(answer.devide())
