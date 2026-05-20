// Task Model Data Architecture Structure
export class Task {
    constructor(title) {
        this.id = Date.now(); // Generates a reliable unique numerical identifier timestamp
        this.title = title;
        this.completed = false; // Default status rule parameter enforcement
    }
}