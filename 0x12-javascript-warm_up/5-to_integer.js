#!/usr/bin/node
const argv = process.argv;
if (isNaN(argv[2])) {
    console.log('Not a number');
} else {
    console.log('MY number: ' + parseInt(argv[2]));
}
