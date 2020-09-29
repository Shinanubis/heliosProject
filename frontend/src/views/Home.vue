<template xmlns:v-if="http://www.w3.org/1999/html">
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div>
    <div v-for="article in articles" :key="article.id">
        {{article.title}}<br>
        {{article.author.username}}<br>
        {{article.content}}<br>
    </div>
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
              id
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
