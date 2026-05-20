// ==========================================
// Core Data Utilities: notesUtil.js
// ==========================================

import fs from 'fs';

const FILE_PATH = 'notes.json';

/**
 * Safely fetches and parses all notes from the local json file database.
 * Demonstrates basic file-reading error handling.
 */
export function getNotes() {
    try {
        // Check if the database file physically exists before attempting execution
        if (!fs.existsSync(FILE_PATH)) {
            return [];
        }
        
        const dataBuffer = fs.readFileSync(FILE_PATH, 'utf-8');
        
        // Handle cases where the file exists but is completely blank
        if (!dataBuffer.trim()) {
            return [];
        }
        
        return JSON.parse(dataBuffer);
    } catch (error) {
        console.error(" -> [System Error]: Failed to read or parse local storage database:", error.message);
        return [];
    }
}

/**
 * Persists changes by stringifying and dumping the array payload back to disk.
 */
export function saveNotes(notesArray) {
    try {
        const jsonPayload = JSON.stringify(notesArray, null, 4);
        fs.writeFileSync(FILE_PATH, jsonPayload, 'utf-8');
    } catch (error) {
        console.error(" -> [System Error]: Failed to write payload changes to disk:", error.message);
    }
}

/**
 * Creates a unique note entry and appends it to the disk repository.
 */
export function addNote(title) {
    const notes = getNotes();
    
    // Check for duplicate titles to enforce business logic validation
    const isDuplicate = notes.some(note => note.title.toLowerCase() === title.toLowerCase());
    
    if (isDuplicate) {
        console.log(`\n❌ Error: A note with the title "${title}" already exists!`);
        return;
    }
    
    notes.push({ title });
    saveNotes(notes);
    console.log(`\n✔ Success! Added new note: "${title}"`);
}

/**
 * Reads the disk payload and cleanly formats entries onto the console output thread.
 */
export function listNotes() {
    const notes = getNotes();
    
    if (notes.length === 0) {
        console.log("\n📁 Your notes repository is currently empty.");
        return;
    }
    
    console.log("\n=================================");
    console.log(`    YOUR ACTIVE NOTES (${notes.length})`);
    console.log("=================================");
    notes.forEach((note, index) => {
        console.log(`${index + 1}. 📝 ${note.title}`);
    });
    console.log("=================================");
}

/**
 * Searches for a note match, filters it out of the array, and updates the file.
 */
export function deleteNote(title) {
    const notes = getNotes();
    const initialLength = notes.length;
    
    // Filter out the requested note
    const updatedNotes = notes.filter(note => note.title.toLowerCase() !== title.toLowerCase());
    
    if (updatedNotes.length === initialLength) {
        console.log(`\n❌ Error: No note found matching the title: "${title}"`);
        return;
    }
    
    saveNotes(updatedNotes);
    console.log(`\n🗑 Success! Deleted note: "${title}"`);
}