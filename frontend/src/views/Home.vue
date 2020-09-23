<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div>
    <table class="table table-striped mt-4">
      <tbody>
        <div v-for="article in articles" :key="article.id">
          <li>Title: {{ article.title }}</li>
          <li>Author: {{ article.author.username }}</li>
          <li>Content: <br>{{ article.content }}</li>
          <br>
        </div>
      </tbody>
    </table>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Home',
  components: {
  },
  data(){
    return {
      articles: []
    }
  },
  async mounted () {
    try {
      let result = await axios({
        method: 'POST',
        url: 'http://127.0.0.1:8000/graphql/',
        data: {
          query: `
          {
            articles{
              title
              author{
                username
              }
              slug
              content
              comment{
                author
                content
                createdAt
              }
              category{
                name
              }
              createdAt
            }
          }	`
        }
      })
      this.articles = result.data.data.articles
    } catch (error) {
      console.error(error)
    }
  }
}
</script>
