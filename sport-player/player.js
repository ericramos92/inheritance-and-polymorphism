class Player{
    constructor(name, age, height, weight){ 
        this._name = name;
        this._age = age;
        this._height = height;
        this._weight = weight;
    }
    get name(){
        return this._name;
    }
    get age(){
        return  `${this._name} is age ${this._age}`;
    }
    get height(){
        return `${this._name} is ${this._height}cm`;
    }
    get weight(){
        return `${this._name} weights ${this._weight}`;
    }
}

const p = new Player('David',25,175,75);

console.log(p.age)
console.log(p.height)
console.log(p.weight)
