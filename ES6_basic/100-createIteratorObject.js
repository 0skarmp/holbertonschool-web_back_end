export default function createIteratorObject(report) {
   employeeIterator() {
    for (const department of Object.keys(report.allEmployees)) {
      for (const employee of report.allEmployees[department]) {
        yield employee;
      }
    }
  }

  return {
    [Symbol.iterator]: employeeIterator,
  };
}
