function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
}

function sillyTheme() {
    document.body.classList.toggle("silly-theme");
}


document.addEventListener('alpine:init', () => {
    
Alpine.data("calendar", () => ({
    calendar: January,
    moveEvent(day_number, dragging) {
        console.log(dragging.day_number);
        // console.log({this.calendar});
        
        const oldDay = this.calendar.get(dragging.day_number);
        const newDay = this.calendar.get(day_number);
        const event = oldDay.events.find((event) => event.name === dragging.name);

            
            oldDay.events = oldDay.events.filter((event) => event.name !== dragging.name);
            newDay.events.push(event);
            console.log({oldDay, newDay});

            document.dispatchEvent(new CustomEvent('calendar-updated'));
            document.querySelector(".dragover").classList.remove('dragover');
    },
    addEvent(day_number) {
        const day = this.calendar.get(day_number);
        const eventName = prompt("Event Name: ");
        if (!eventName) {
            return;
        } 
        if (day.events.find((event) => event.name === eventName)) {
            if (!confirm("Event already exists! do you want to replace it?")){
                return;
            }
        }
        day.events.push({
            "name": eventName,
            "startTime": prompt("Start Time: "),
            "endTime": prompt("End Time: "),
            "description": prompt("Description: ")
        });
    },
    deleteEvent(day_number, event_name) {
        const day = this.calendar.get(day_number);
        day.events = day.events.filter((event) => event.name !== event_name);
    },
    dragging: null
}))

})


  