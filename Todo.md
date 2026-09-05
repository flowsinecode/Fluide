# Todo

- [X] Make an UI
- [] Make a menu to let it work
- [] Build-in runner
- [] Syntax highlight (for flu, not python)
- [] Settings
- [] Complete Fluide
- [] Test it
- [] Build file!

### Update
nglam - founder of Fluentix - confirm that this IDE will be official if I finished it!

# Bug Fix TODO

## Critical Bugs

- [ ] Implement the Run action; the current runner does nothing.
- [ ] Connect the detected Flu compiler path to the runner.
- [ ] Show a clear error when the Flu compiler cannot be found or cannot be started.
- [ ] Handle errors when opening a file from the command line.
- [ ] Handle errors when saving a file, including permission errors and locked files.
- [ ] Prevent unsaved changes from being lost when creating or opening another file.

## File Handling

- [ ] Confirm the file format and encoding before opening a file.
- [ ] Handle files that do not exist or cannot be read.
- [ ] Handle multiple compiler paths returned by the system.
- [ ] Avoid adding an unintended newline when saving file content.
- [ ] Keep the current file path and displayed file name synchronized after Save As.

## Terminal and Runner

- [ ] Expose terminal input and output so the runner can use them.
- [ ] Display compiler output and errors in the terminal panel.
- [ ] Add a way to stop a running program.
- [ ] Prevent the UI from freezing while a program is running.
- [ ] Disable or update Run controls while a program is active.

## Menu Actions

- [ ] Implement Theme settings.
- [ ] Implement Editor settings.
- [ ] Implement Help.
- [ ] Implement Zen mode.
- [ ] Implement Full Screen mode.
- [ ] Implement Go to Line.
- [ ] Implement Back and Forward navigation.

## Reliability and Testing

- [ ] Show a useful message when a required dependency is missing.
- [ ] Test startup with and without the Flu compiler installed.
- [ ] Test opening valid, missing, unreadable, and invalid-encoding files.
- [ ] Test saving new and existing files, including failed saves.
- [ ] Test every menu action and canceling every file dialog.
- [ ] Add regression tests for fixed bugs.

## Existing Features

- [ ] Add Flu syntax highlighting instead of Python syntax highlighting.
- [ ] Complete the settings system.
- [ ] Build and package Fluide.