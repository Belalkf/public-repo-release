# Contributing

Keep changes focused and preserve publication permissions. Test with synthetic temporary repositories; never use credentials or real private reports as fixtures. Corrected script defects need regression tests. Python 3.9 is the minimum; the helper uses only the standard library and installed Git.

Run the two commands in [README](README.md#validate). CI repeats them on Python 3.9 and 3.14 on Linux, and Python 3.14 on macOS and Windows. Open a pull request; all four test jobs must pass on the current base, and review conversations must be resolved. CodeQL also blocks high-or-higher security findings and standard errors. A solo maintainer can merge without approving their own pull request. Automatic merging is off.

Keep documentation paragraphs unwrapped, keep each subject in its own document, and include every runtime reference inside the installable skill folder. Update [validation limits](VALIDATION.md) when coverage changes. Helper tests establish concrete script behaviour, not an agent's judgment or a complete security audit.
