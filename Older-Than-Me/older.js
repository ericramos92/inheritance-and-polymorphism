class Person {
	constructor(name, age) {
		this._name = name;
		this._age = age;
	}
		
	compareAge(other) {
		if(this._age === other._age) {
			return `${other._name} is the same age as me.`
		}
		if(this._age > other._age) {
			return `${other._name} is younger than me.`
		}
		return `${other._name} is older than me.`
	}
}
const p1 = new Person("Samuel", 24)
const p2 = new Person("Joel", 36)
const p3 = new Person("Lily", 24)
console.log(p1.compareAge(p2));
console.log(p2.compareAge(p1));
console.log(p1.compareAge(p3))