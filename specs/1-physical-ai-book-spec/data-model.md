# Data Model: Physical AI Book

## Book Chapter
- **chapterId** (string): Unique identifier for the chapter
- **title** (string): Title of the chapter
- **description** (string): Brief description of the chapter content
- **lessons** (array): List of lessons within the chapter
- **prerequisites** (array): Prerequisites needed for the chapter
- **learningObjectives** (array): Learning objectives for the chapter

## Lesson
- **lessonId** (string): Unique identifier for the lesson
- **title** (string): Title of the lesson
- **content** (string): Main content of the lesson in MDX format
- **handsOnExamples** (array): List of hands-on examples in the lesson
- **challenges** (array): List of challenges at the end of the lesson
- **duration** (number): Estimated time to complete the lesson (minutes)

## HandsOnExample
- **exampleId** (string): Unique identifier for the example
- **title** (string): Title of the example
- **description** (string): Description of what the example demonstrates
- **codeFile** (string): Path to the code file for the example
- **dependencies** (array): List of required dependencies for the example

## Challenge
- **challengeId** (string): Unique identifier for the challenge
- **title** (string): Title of the challenge
- **description** (string): Description of the challenge
- **difficulty** (string): Difficulty level (beginner, intermediate)
- **solution** (string): Path to the solution (optional, for reference)

## Learning Objective
- **objectiveId** (string): Unique identifier for the objective
- **description** (string): Description of what the learner should understand
- **relatedChapter** (string): Chapter this objective belongs to
- **relatedLesson** (string): Lesson this objective belongs to