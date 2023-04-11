function Circlewide1(a){
    let circle_w =  a*a*3.14;
    return circle_w
}
console.log(Circlewide1(2));

const Num_max = function(arr){
    let num_M = arr[0];
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > num_M) {
          num_M = arr[i];
        }
      }
return num_M
}
let b = [4,7,9,2,8,3]
console.log(Num_max(b));

function BMI(hight, weight){
    let bmi = weight/(hight/100)**2;
    if (bmi >= 26)
        console.log(`비만`)
    else if ((bmi < 26) && (bmi >= 24))
        console.log(`과체중`)
    else if ((bmi < 24) && (bmi >= 18))
        console.log(`정상`)
    else
        console.log(`저체중`)

}
BMI(190,116);
