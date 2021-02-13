"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.hello = void 0;
const world = "world";
function hello(word = world) {
    return `Hello ${word}! `;
}
exports.hello = hello;
console.log(hello("Erik"));
//# sourceMappingURL=index.js.map