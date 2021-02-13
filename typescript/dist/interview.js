"use strict";
//
// Function Specification
//
// The medianAgeForDiagnosis function return the median age per diagnosis given 
// an array of diagnosis-age pairs.  
//
// It must:
//
// - Return an object with dianosis keys, and median age values
// - Handle multiple pairs
// - Handle empty case
//
function medianAgeForDiagnosis(pairs) {
    // Empty case
    if (pairs === undefined || pairs.length === 0) {
        return {};
    }
    // Handle multiple pairs
    let diagnoses = new Map();
    pairs.forEach(element => {
        let code = element[0];
        let age = element[1];
        if (diagnoses.has(code)) {
            diagnoses.get(code).push(age);
        }
        else {
            diagnoses.set(code, []);
            diagnoses.get(code).push(age);
        }
    });
    console.log(diagnoses);
    // Return an object with dianosis keys, and median age values
    return {};
}
let test_pairs = [['nsf', 34], ['tb', 45]];
medianAgeForDiagnosis(test_pairs);
//# sourceMappingURL=interview.js.map