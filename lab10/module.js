/** Class repesenting operation
 * @param {number} x - first value
 * @param {number} y - second value
 */
class Operation {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
    /** Method sum()
     * @returns x + y  - sum of the two arguments in class constructor
     */
    sum() {
        return this.x + this.y;
    }
}

module.exports = {
    Operation
}