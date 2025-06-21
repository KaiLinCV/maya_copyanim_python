# Maya Copy Animation Tool

## 🛠️ Overview

This is a Python script for Autodesk Maya that lets you **copy animation keyframes** from one rig to another with ease. I originally created this tool to automate the repetitive task of copying and pasting animation between files at work, which was something that used to take up more time than it should.

By streamlining this process, the tool helps improve workflow efficiency, especially when working with characters that share similar rig structures or naming conventions.

---

## Goals for creating this script

- Ability to copy animation from the source to the target through the use of controllers.
- Select nested controllers in both the source and target controller rigs.  
- Works with or without namespaces.  
- Create a simple user-friendly UI to run the script 

---

## 📘 Documentation

Want to see how this script was made?  
👉 [Check out the full development walkthrough and design decisions](./documentation/process.md)

---

## 🚀 How to Use

1. Open Autodesk Maya and load the script:
   - You can drag and drop the script into the Script Editor or add it to your shelf.
2. Run the script — a UI will appear.
3. Set the **source root** (controller group to copy from).
4. Set the **target root** (controller group to paste onto).
5. Click **Copy Animation** and the keyframes will be transferred.

> ⚠️ Ensure both rigs share the same controller naming structure.

---

## ✅ Conclusion

Creating this tool helped me:
- Practice and deepen my understanding of **Python scripting** within Maya.
- Solve real-world production problems by automating repetitive animation workflows.
- Work with **scene hierarchy traversal**, **UI design**, and **namespace handling**.

This script is part of my ongoing journey into combining technical artistry with tool development to improve animation pipelines.

---

