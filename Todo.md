# Fluide Learning Roadmap / Lộ trình học và phát triển Fluide

> **Teacher's note / Lời thầy:** Build one small, understandable piece at a time. Before writing code, explain the behavior in your own words, identify the owner of that behavior, and decide how you will prove it works.
>
> Hãy xây từng phần nhỏ, dễ hiểu. Trước khi viết code, hãy tự diễn giải hành vi, xác định module chịu trách nhiệm, rồi chọn cách chứng minh nó hoạt động.

## How to use this file / Cách sử dụng

- [ ] Do the tasks in order unless a task is explicitly marked as optional.
- [ ] Complete the **Learn** questions before checking an item as done.
- [ ] Keep each change small enough to explain in one short paragraph.
- [ ] After every behavior change, test both the normal path and one failure path.

---

## Phase 0 - Understand the project / Hiểu dự án

### 0.1 Draw the application map / Vẽ bản đồ ứng dụng

- **What / Việc gì:** Trace the path from `main.py` to the editor, action bar, file helpers, and terminal.
- **Why / Tại sao:** A clear ownership map prevents UI code from quietly becoming application logic.
- **Learn / Câu hỏi:** Which module creates the window? Which object owns the current file path? Where should running a program begin?
- **Done / Hoàn thành khi:** You can explain the startup flow and the responsibility of every file in `core/` and `ui/` without opening the code.

### 0.2 Define the first useful version / Xác định phiên bản đầu tiên có ích

- **What / Việc gì:** Write a short definition of Fluide's minimum usable workflow: open, edit, save, run, and read output.
- **Why / Tại sao:** A small target makes priorities and trade-offs visible.
- **Learn / Câu hỏi:** What must work for a user to finish one Flu program? Which features can wait?
- **Done / Hoàn thành khi:** The workflow fits in five or fewer steps and has clear success and failure outcomes.

---

## Phase 1 - Make the editor reliable / Làm trình soạn thảo đáng tin cậy

### 1.1 Establish the file state / Quản lý trạng thái file

- **What / Việc gì:** Distinguish a new document, a saved document, and a modified document.
- **Why / Tại sao:** Users must know whether their work is safe before they run or close the IDE.
- **Learn / Câu hỏi:** What does `Untitled` mean? When should the window show a modified state? What happens if saving is cancelled?
- **Done / Hoàn thành khi:** New, open, save, save-as, and cancel flows preserve the correct file name and content.

### 1.2 Handle errors as user actions / Xử lý lỗi như một phần của trải nghiệm

- **What / Việc gì:** Define friendly responses for a missing file, unreadable file, failed save, and invalid path.
- **Why / Tại sao:** A robust editor explains what happened and what the user can do next.
- **Learn / Câu hỏi:** Which errors can be recovered from? Which details belong in a dialog, and which belong in a log?
- **Done / Hoàn thành khi:** Each expected file error gives a clear message and leaves the editor in a usable state.

### 1.3 Choose the language experience / Chọn trải nghiệm ngôn ngữ

- **What / Việc gì:** Verify that syntax highlighting and editor behavior match Flu rather than silently pretending the document is Python.
- **Why / Tại sao:** Editor feedback teaches the language and should not mislead the developer.
- **Learn / Câu hỏi:** What language support does the editor library provide? What is the fallback when Flu support is unavailable?
- **Done / Hoàn thành khi:** A Flu file has an intentional highlighting strategy documented in this roadmap.

---

## Phase 2 - Run Flu programs safely / Chạy chương trình Flu an toàn

### 2.1 Specify the run contract / Đặc tả hợp đồng của nút Run

- **What / Việc gì:** Describe the exact sequence: validate document, save if needed, locate the compiler, start the process, and display the result.
- **Why / Tại sao:** The Run button should be a predictable workflow, not a collection of hidden side effects.
- **Learn / Câu hỏi:** Can an unsaved document run? What should happen when the compiler is missing? How is the exit code interpreted?
- **Done / Hoàn thành khi:** The contract covers success, compiler-not-found, compile error, runtime error, and user cancellation.

### 2.2 Separate process control from UI / Tách điều khiển process khỏi UI

- **What / Việc gì:** Keep compiler execution and process state in `core/`; let the UI display state and output.
- **Why / Tại sao:** This separation makes the runner testable and keeps the interface responsive.
- **Learn / Câu hỏi:** Which data crosses the boundary: command, output, error, exit code, or status? How will the UI receive it?
- **Done / Hoàn thành khi:** The runner can be reasoned about without creating a window, and the UI does not construct compiler commands itself.

### 2.3 Add output and stop behavior / Thêm output và dừng chương trình

- **What / Việc gì:** Display standard output and errors, then provide a separate Stop action for a running process.
- **Why / Tại sao:** Output is feedback; stopping is control. They should not be hidden inside the Run action.
- **Learn / Câu hỏi:** How do you avoid freezing the window? What happens to child processes? What status is shown after Stop?
- **Done / Hoàn thành khi:** A long-running program can be observed and stopped without closing Fluide.

---

## Phase 3 - Finish the core IDE workflow / Hoàn thiện quy trình IDE cốt lõi

### 3.1 Make menus honest / Làm menu đúng với chức năng

- **What / Việc gì:** Implement or clearly disable menu items such as Zen mode, Full Screen, Go to Line, Back, and Forward.
- **Why / Tại sao:** A visible command creates a promise; unfinished commands should not look complete.
- **Learn / Câu hỏi:** Which commands need editor history? Which need window state? What is the smallest useful implementation?
- **Done / Hoàn thành khi:** Every visible menu command works, is intentionally deferred, or is clearly unavailable.

### 3.2 Add unsaved-change protection / Bảo vệ thay đổi chưa lưu

- **What / Việc gì:** Confirm before New, Open, Exit, or replacing content when changes have not been saved.
- **Why / Tại sao:** Losing source code is more serious than a small inconvenience in the interface.
- **Learn / Câu hỏi:** What are the three choices: save, discard, cancel? What should happen when saving fails?
- **Done / Hoàn thành khi:** No destructive navigation can silently discard edits.

### 3.3 Define settings boundaries / Xác định ranh giới cài đặt

- **What / Việc gì:** Decide which settings belong in `assets/config.json`: theme, font, editor options, compiler path, or other preferences.
- **Why / Tại sao:** A settings file should have a stable contract instead of becoming a miscellaneous storage box.
- **Learn / Câu hỏi:** Which values are user preferences? What are safe defaults? How are invalid settings recovered?
- **Done / Hoàn thành khi:** Each setting has a type, default, persistence rule, and validation rule.

---

## Phase 4 - Quality and maintainability / Chất lượng và khả năng bảo trì

### 4.1 Create a manual test checklist / Tạo checklist kiểm thử thủ công

- **What / Việc gì:** Record tests for new file, open, save, save-as, run, compiler missing, compile failure, runtime failure, and stop.
- **Why / Tại sao:** A repeatable checklist catches regressions faster than memory.
- **Learn / Câu hỏi:** What is the input, expected result, and cleanup step for each test?
- **Done / Hoàn thành khi:** Another developer can execute the checklist without asking what “works” means.

### 4.2 Add focused automated tests / Thêm test tự động có trọng tâm

- **What / Việc gì:** Test file-state logic and command construction independently from the GUI where practical.
- **Why / Tại sao:** Small logic tests are faster and more reliable than testing every behavior through a window.
- **Learn / Câu hỏi:** Which logic is deterministic? Which parts require integration testing with the actual Flu compiler?
- **Done / Hoàn thành khi:** The most failure-prone core behavior has a repeatable automated check.

### 4.3 Document setup and limitations / Ghi lại cài đặt và giới hạn

- **What / Việc gì:** Update `README.md` with dependencies, Flu compiler setup, supported workflow, and known limitations.
- **Why / Tại sao:** A project is easier to maintain when a new contributor can reproduce its environment.
- **Learn / Câu hỏi:** Can a new developer run Fluide from a clean machine using only the README?
- **Done / Hoàn thành khi:** Setup instructions are tested by someone who did not write them.

---

## Teacher's review questions / Câu hỏi tự vấn của người học

Before calling a phase complete, answer these in writing:

1. **What behavior changed? / Hành vi nào đã thay đổi?**
2. **Which module owns it? / Module nào chịu trách nhiệm?**
3. **What can fail? / Những trường hợp nào có thể lỗi?**
4. **How did I verify it? / Tôi đã kiểm chứng bằng cách nào?**
5. **What did I deliberately postpone? / Tôi đã chủ động hoãn điều gì?**

> **Rule / Quy tắc:** Do not mark a task complete because the code exists. Mark it complete when the behavior is understandable, testable, and useful to the person using Fluide.
