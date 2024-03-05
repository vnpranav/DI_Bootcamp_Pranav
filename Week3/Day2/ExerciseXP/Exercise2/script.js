const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
var myWatchedSeriesLength = myWatchedSeries.length;
console.log("Part 1");
console.log("I have watched", myWatchedSeriesLength, "series :", myWatchedSeries[0], myWatchedSeries[1], myWatchedSeries[2]);
console.log("***********");
console.log("Part 2");
let newWatchedSeries = myWatchedSeries;
newWatchedSeries.push("how i met your mother");
newWatchedSeries.unshift("one piece");
removed = newWatchedSeries.splice(2,1);
console.log(removed.toString().substr(2,1));
console.log("I have watched", newWatchedSeries.length, "series:", newWatchedSeries.join());


