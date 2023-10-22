export default function createEmployeesObject(departmentName, employees) {
  const pictionary = {
    [departmentName]: employees,
  };
  return pictionary;
}
