//React query testing.
import { useQuery, useQueryClient, QueryClient } from 'react-query';
const queryStringPreamble = 'http://142.93.125.94:5000/q/'
var upc = "049000050103"
var queryString = queryStringPreamble + upc
console.log("Query string is: ", queryString)
var queryResult = fetch(queryString)
console.log(queryResult);