name := "scala"

version := "0.1"

scalaVersion := "2.12.7"

libraryDependencies += "junit" % "junit" % "4.10" % Test
libraryDependencies += "org.scalactic" %% "scalactic" % "3.0.5"
libraryDependencies += "org.scalatest" %% "scalatest" % "3.0.5" % "test"

// set the main class for the main 'sbt run' task
// mainClass in (Compile, run) := Some("chandrima_xor")