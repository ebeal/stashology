import React from 'react';


const Todo = ({todo, remove}) => {
    return (<li onClick={() => {remove(todo.id)}}>{todo.text}{todo.id}</li>);
}
// export class TodoList extends React.Component {
//     constructor(props) {
//         super(props);
//         this.todoNode = this.props.todos.map((todo) => {
//             return (<Todo todo={todo} key={todo.id} remove={this.props.remove}/>)
//         });
//     }
//     render() {
//         return(<ul>{this.todoNode}</ul>);
//     };
// };

export const TodoList =({todos, remove}) => {
  const todoNode = todos.map((todo) => {
    return (<Todo todo={todo} key={todo.id} remove={remove}/>)
  });
  return (<ul>{todoNode}</ul>);
}