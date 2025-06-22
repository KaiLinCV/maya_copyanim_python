# Maya Copy Animation Tool

## 🛠️ Overview

This is a Python script for Autodesk Maya that lets you **copy animation keyframes** from one rig to another with ease. I originally created this tool to automate the repetitive task of copying and pasting animation between files at work, since it was something that used to take up more time than it should.

By streamlining this process, the tool helped me improve workflow efficiency and reduce manual errors.

![CopyAnim](./screenshots/copy_anim_sample.gif)

---

## 📝 Goals for creating this script

- Copy animation from a source rig to a target rig based on matching controller names.
- Automatically gather **nested controllers** from both source and target hierarchies.
- Handle rigs with or without **namespaces**.
- Build a clean, user-friendly **UI** to make the tool easy to use.

---

## 📘 Documentation

Want to see how this script was made?  
[Check out the full development walkthrough and design decisions](./documentation/process_doc.md)

---

## 📜 How to Use

1. Open Autodesk Maya and load the script:
   - You can drag and drop the script into the Script Editor or add it to your shelf.
2. Run the script, an UI will appear.
3. Set the **source root** (controller group to copy from).
4. Set the **target root** (controller group to paste onto).
5. Click **Copy Animation** and the keyframes will be transferred.

> **Note:** Ensure both rigs share the same controller naming structure.

---

## ✅ Conclusion

Creating this tool was a valuable learning experience that allowed me to apply practical Python scripting within Maya. It helped me strengthen my understanding of Maya’s command system and API. I also gained experience writing modular and reusable functions to solve production-focused problems. In addition, I became more confident working with both **Python** and **MEL-compatible commands** to automate tasks inside Maya.

I’m proud of how this script turned out. It’s a practical, easy to use, and has already improved animation workflows in my day-to-day work. It also gave me a stronger foundation for developing more advanced tools in the future.


