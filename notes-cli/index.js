// ==========================================
// CLI Routing Entry Point: index.js
// ==========================================

import { addNote, listNotes, deleteNote } from './notesUtil.js';

// process.argv[0] is the Node execution path
// process.argv[1] is the index.js file path
// process.argv[2] is the command string (add, list, delete)
// process.argv[3] is the target user value (e.g., Note title text string)
const command = process.argv[2];
const targetValue = process.argv[3];

if (!command) {
    printUsageGuide();
    process.exit(0);
}

// Route processing commands to their respective functionality handlers
switch (command.toLowerCase()) {
    case 'add':
        if (!targetValue) {
            console.log("\n❌ Error: Please provide a note title! Example: node index.js add \"Buy Groceries\"");
        } else {
            addNote(targetValue);
        }
        break;
        
    case 'list':
        listNotes();
        break;
        
    case 'delete':
        if (!targetValue) {
            console.log("\n❌ Error: Please provide the exact title of the note to delete! Example: node index.js delete \"Buy Groceries\"");
        } else {
            deleteNote(targetValue);
        }
        break;
        
    default:
        console.log(`\n❌ Error: Unknown action instruction sequence command: "${command}"`);
        printUsageGuide();
        break;
}

// Help documentation text block fallback
function printUsageGuide() {
    console.log("\n========================================================");
    console.log("       Core Node.js CLI Notes Manager - Usage Guide     ");
    console.log("========================================================");
    console.log(" Available Commands:");
    console.log("   node index.js add \"Your Note Content\"  -> Create a note");
    console.log("   node index.js list                      -> Display all notes");
    console.log("   node index.js delete \"Your Note Title\" -> Remove a note");
    console.log("========================================================");
}