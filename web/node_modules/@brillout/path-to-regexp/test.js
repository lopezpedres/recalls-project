const matchPath = require('./');

console.log(matchPath('/hello/jon', {path: '/hello/:name', exact: true}));
