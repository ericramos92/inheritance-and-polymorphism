class Point{
    constructor(x,y){
        this.x=x;
        this.y=y;
    }
    toString(){
        return `[x=${this.x},y=${this.y}]`
    }
}

const p = new Point(1,2);
console.log(p.toString());