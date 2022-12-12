import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state = {
    posts: []
  }


  componentDidMount() {
    this.loadPosts()
  }

  loadPosts = async () => {
    const postResponse = fetch('https://jsonplaceholder.typicode.com/posts')
    const photoResponse = fetch('https://jsonplaceholder.typicode.com/photos')

    const [posts, photos] = await Promise.all([postResponse, photoResponse])

    const postJson = await posts.json()
    const photosJson = await photos.json()

    const postsAndPhotos = postJson.map((post, index) => {
      return { ...post, cover: photosJson[index].url}
    })

    this.setState({ posts: postsAndPhotos })
  }

  render() {
    const { posts } = this.state
    //const name = this.state.name

    return (
      <section className='container'>
        <div className="posts">
          {posts.map(posts => (
            <div className='post'>
              <img src={posts.cover} alt={posts.title}></img>
              <div className='post-content' key={posts.id}>
                <h2>{posts.title}</h2>
                <p>{posts.body}</p>
              </div>
            </div>
          ))}
        </div>
      </section>
    );
  }
}

export default App;
