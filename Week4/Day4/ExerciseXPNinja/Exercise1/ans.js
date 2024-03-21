const numPages = Math.ceil((dayStart + daysMonth) / 7);


    // Create the table pages
  
    for (let i = 0; i < numPages; i++) {
  
      const page = document.createElement('tr');
  
      for (let j = 0; j < 7; j++) {
  
        const day = (i * 7 + j + 2) - dayStart;
  
        if (day > 0 && day <= daysMonth) {
  
          const td = document.createElement('td');
  
          td.textContent = day;
  
          page.appendChild(td);
  
        } else {
  
          const td = document.createElement('td');
  
          td.textContent = '';
  
          page.appendChild(td);
  
        }
  
      }
  
      table.appendChild(page);
  
  
      if ((i + 1) % 2 === 0) {
  
        table.appendChild(document.createElement('tbody'));
  
      }

    document.body.appendChild(table);
}

