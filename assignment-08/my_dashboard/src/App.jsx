import { useState } from "react";

function App() {
  // State: Map of id → student
  const [studentsMap, setStudentsMap] = useState(new Map());
  const [name, setName] = useState("");
  const [coursesInput, setCoursesInput] = useState("");
  const [gpa, setGpa] = useState("");
  const [filterCourse, setFilterCourse] = useState("");

  // Add new student
  const addStudent = () => {
    if (!name || !coursesInput || !gpa) return;

    const id = Date.now();

    const newStudent = {
      id,
      name,
      enrolledCourses: new Set(coursesInput.split(",").map(c => c.trim())),
      gpa: parseFloat(gpa)
    };

    const newMap = new Map(studentsMap); // copy (no mutation)
    newMap.set(id, newStudent);

    setStudentsMap(newMap);

    setName("");
    setCoursesInput("");
    setGpa("");
  };

  // Remove student
  const removeStudent = (id) => {
    const newMap = new Map(studentsMap);
    newMap.delete(id);
    setStudentsMap(newMap);
  };

  // Convert Map → Array
  const studentsArray = Array.from(studentsMap.values());

  // Sort by GPA (descending)
  const sortedStudents = [...studentsArray].sort((a, b) => b.gpa - a.gpa);

  // Filter by course
  const filteredStudents = filterCourse
    ? sortedStudents.filter(student =>
        student.enrolledCourses.has(filterCourse)
      )
    : sortedStudents;

  // Unique courses using reduce + Set
  const uniqueCourses = studentsArray.reduce((acc, student) => {
    student.enrolledCourses.forEach(course => acc.add(course));
    return acc;
  }, new Set());

  return (
    <div style={{ padding: "20px" }}>
      <h2>Course Enrollment Dashboard</h2>

      {/* Add Student */}
      <input
        placeholder="Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <input
        placeholder="Courses (comma separated)"
        value={coursesInput}
        onChange={(e) => setCoursesInput(e.target.value)}
      />
      <input
        placeholder="GPA"
        type="number"
        step="0.1"
        value={gpa}
        onChange={(e) => setGpa(e.target.value)}
      />
      <button onClick={addStudent}>Add Student</button>

      <hr />

      {/* Filter */}
      <input
        placeholder="Filter by course"
        value={filterCourse}
        onChange={(e) => setFilterCourse(e.target.value)}
      />

      <h3>Students (Sorted by GPA)</h3>
      {filteredStudents.map(student => (
        <div key={student.id} style={{ border: "1px solid gray", margin: "10px", padding: "10px" }}>
          <p>Name: {student.name}</p>
          <p>GPA: {student.gpa}</p>
          <p>
            Courses: {Array.from(student.enrolledCourses).join(", ")}
          </p>
          <button onClick={() => removeStudent(student.id)}>
            Remove
          </button>
        </div>
      ))}

      <hr />

      <h3>All Unique Courses</h3>
      <ul>
        {Array.from(uniqueCourses).map((course, index) => (
          <li key={index}>{course}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
