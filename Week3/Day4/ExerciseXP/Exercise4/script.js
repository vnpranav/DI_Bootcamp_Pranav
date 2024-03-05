const users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
len = users.length;
var online = "";
switch (len) {
    case 0:
        online = "no one is online";
        break;
    case 1:
        online = users[0] + " is online";
        break;
    case 2:
        online = users[0] + ", " + users[1] + " are online";
        break;
    default:
        online = users[0] + ", " + users[1] + " and " + `${len - 2} more are online`;
        break;
}
console.log(online);