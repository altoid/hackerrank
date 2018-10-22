name := "scala"

version := "0.1"

scalaVersion := "2.12.7"

// set the main class for the main 'sbt run' task
mainClass in (Compile, run) := Some("superpowers")