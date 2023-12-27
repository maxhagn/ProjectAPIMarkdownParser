# Regions Of Interest Profiler (Bachelor Thesis)

![Thumbnail](https://files.hagn.network/images/regions-of-interest-profiler/thumbnail.webp)

A tool from my bachelor's thesis 'Detecting Performance Bottlenecks Through AST Transformations', adding performance counters to C++ code for bottleneck analysis, built with Clang's LibTooling library.


---
Ein Tool aus meiner Bachelorarbeit 'Erkennen von Leistungsengpässen durch AST-Transformationen', das Leistungszähler in C++-Code einfügt, um Engpässe zu analysieren, entwickelt mit Clangs LibTooling-Bibliothek.

## Key Facts

- University Low Level Development Project
- 35 Workdays
- Language: English
- Team Size: 2

### Roles

- Software Engineer

## Project Goals

The project's main goal was to develop a tool that dynamically transforms C++ code by inserting performance counters, enabling users to step-by-step examine a program for performance bottlenecks. Each profiling step involves detailed examination at different levels, providing users with performance statistics to identify critical regions for further investigation.


---
Hauptziel des Projekts war die Entwicklung eines Tools, das C++-Code dynamisch transformiert, indem es Leistungszähler einfügt. Dies ermöglicht es dem Benutzer, schrittweise ein Programm auf Leistungsengpässe zu untersuchen. Jeder Profilierungsschritt beinhaltet eine detaillierte Untersuchung auf verschiedenen Ebenen und liefert dem Benutzer Statistiken zur Leistung des Programms, um kritische Bereiche für weitere Untersuchungen zu identifizieren.

## Experience

Written in C++, the tool leverages the capabilities of the Clang compiler frontend for tool creation. It allows for fine-grained analysis by traversing functions and statements in the Clang AST and annotating them as needed. The tool supports options for specifying traversal entry points and outputs the modified code to an 'output.cpp' file or a user-specified file. This project, as detailed in the 'Publications' section of my bachelor thesis, represents a significant contribution to performance analysis in software development.


---
Das in C++ geschriebene Tool nutzt die Möglichkeiten des Clang-Compiler-Frontends zur Tool-Erstellung. Es ermöglicht eine detaillierte Analyse, indem es Funktionen und Anweisungen im Clang-AST durchläuft und bei Bedarf annotiert. Das Tool unterstützt Optionen zur Spezifizierung von Einstiegspunkten für die Traversierung und gibt den modifizierten Code in einer 'output.cpp'-Datei oder einer vom Benutzer spezifizierten Datei aus. Dieses Projekt, das im Abschnitt 'Publikationen' meiner Bachelorarbeit detailliert beschrieben ist, stellt einen bedeutenden Beitrag zur Leistungsanalyse in der Softwareentwicklung dar.

## Skills

### Programming Languages

 - C++
### Technologies

 - UNIX
 - CMake
 - Clang
 - GCC
 - Latex
### Soft Skill

 - Scientific Writing

## Visite

- [GitHub Repository](https://github.com/maxhagn/ROIProfilerCPP)
- [Website](https://roiprofiler.hagn.network)

## Gallery

![Image 01 Title Page](https://files.hagn.network/images/regions-of-interest-profiler/title-page.webp)
![Image 02 Example Code Showing a Simple C++ Application](https://files.hagn.network/images/regions-of-interest-profiler/example-code-cpp.webp)
![Image 03 Example Code Showing the Instructions Wrapped by Performance Counters](https://files.hagn.network/images/regions-of-interest-profiler/example-code-instructions-wrapped.webp)
![Image 04 The Desired Output of the Transformed Application](https://files.hagn.network/images/regions-of-interest-profiler/output-regions-of-interest-profiler.webp)
![Image 05 An Example of the Abstract Syntax Tree Provided by Clang](https://files.hagn.network/images/regions-of-interest-profiler/example-abstract-syntax-tree-clang.webp)
![Image 06 Flow Chart Representing the Logic of the ROIProfiler](https://files.hagn.network/images/regions-of-interest-profiler/roiprofiler-flow-chart.webp)
![Image 07 The Synopsis of the ROIProfiler](https://files.hagn.network/images/regions-of-interest-profiler/roiprofiler-synopsis.webp)
![Image 08 Runtime Comparison for the Varying Loop Runtimes Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-forloop-comparison.webp)
![Image 09 Runtime Deviation for the Execution of the Varying Loop Runtimes Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-forloop-deviation.webp)
![Image 10 Runtime Comparison for the Fibonacci Sequence Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-fibonacci-comparison.webp)
![Image 11 Runtime Comparison for the Password Generator Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-password-comparison.webp)
![Image 12 Runtime Comparison for the Variable Password Size Generator Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-variable-password-comparison.webp)
![Image 13 Time Per Measurement Value Comparison for Various Test Cases](https://files.hagn.network/images/regions-of-interest-profiler/stats-conclusion-per-counter.webp)
![Image 14 Total Overhead Per Code Block Comparison for Various Test Cases](https://files.hagn.network/images/regions-of-interest-profiler/stats-conclusion-per-array-entry.webp)
![Image 15 Prime Number Comparison for the Prime Benchmark Application](https://files.hagn.network/images/regions-of-interest-profiler/stats-prime-comparison.webp)

