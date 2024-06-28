function divCon(x){
    let sum_of_integers = 0;
    let sum_of_strings = 0;


    for (let increment = 0;increment < x.length; increment++){
        if(typeof(x[increment]) === "number"){
            sum_of_integers += x[increment]
         
        }
        else if(typeof(x[increment]) === "string"){
            sum_of_strings += parseInt(x[increment])
        }
    }

    return (sum_of_integers - sum_of_strings)
}


x = [20,"70",10]
console.log(divCon(x))
