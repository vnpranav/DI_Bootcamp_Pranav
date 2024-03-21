function createCalendar(year, month)
{
    let table = document.createElement("table");

    let tableHead = document.createElement("thead");
    const weekDays = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

    for (week of weekDays)
    {
        let th = document.createElement("th");
        th.textContent = week;
        th.style.fontSize = "medium";
        th.style.padding = "5px"

        tableHead.appendChild(th);
    }
    table.appendChild(tableHead);

    let daysMonth = new Date(year, month, 0).getDate();
    let dayStart = new Date(year,month,1).getDay();
    if (dayStart == 0) {
        dayStart = 6;
    } else {
        dayStart = dayStart - 1
    }

    

    document.body.appendChild(table);
}
createCalendar(2023,1)
