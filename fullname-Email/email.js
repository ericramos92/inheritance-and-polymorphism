class Employee{
    constructor(first,last){
        this._first=first;
        this._last=last;
    }
    get first(){
        return this._first;
    }
    get last(){
        return this._last;
    }
    get email(){
        return `${this._first}.${this._last}@company.com`.toLowerCase();
    }
    get fullname(){
        return `${this._first} ${this._last}`;
    }
}
const emp1 = new Employee('John','Smith');
console.log(emp1.fullname);
const emp2 = new Employee("Mary",  "Sue");
console.log(emp2.email);
const emp3 = new Employee("Antony", "Walker");
console.log(emp3.first);