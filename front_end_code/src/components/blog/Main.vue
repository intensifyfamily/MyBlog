<template>
  <div>
    <el-row :gutter="30">
      <el-col :span="17">
        <div class="">
          <div class="selection_title">
            <div class="title_left">
              <img class="left_item" src="../../assets/logo.png" width="60" height="60" alt="">
              <h2 class="left_item">文章 | Articles</h2>
              <a class="left_item" href="">View more ></a>
            </div>
            <div class="title_right">
              <div class=" right_item"><a href="" v-on:click.prevent @click="getArticleList()"><i class="el-icon-refresh-left"></i></a></div>
              <el-menu :default-active="activeIndex" class="right_item" mode="horizontal" @select="handleSelect">
                <el-menu-item index="1">最新</el-menu-item>
                <el-menu-item index="2">点赞最多</el-menu-item>
                <el-menu-item index="3">推荐</el-menu-item>
              </el-menu>
            </div>
          </div>
          <el-card class="article_img"><img src="../../assets/images/aritcle_top.jpg" width="100%" alt=""></el-card>
          <el-card class="article" v-for="item in articles" :key="item.id">
              <a href="" v-on:click.prevent @click="clickTitle(item.id)">{{item.title}}</a>
              <div style="margin: 10px 0">
                <el-tag :type="tag.type" v-for="tag in item.tag_list" :key="tag.id">{{tag.content}}</el-tag>
              </div>
              <p class="desc"><span>{{item.desc}}</span><a href="" v-on:click.prevent @click="clickTitle(item.id)">查看更多></a></p>
              <p class="operate_info">
                <span>{{item.create_time | dateFormat}}</span>
                <span><i class="el-icon-view"></i>{{item.view}}</span>
                <span><i class="el-icon-star-on"></i>{{item.like}}</span>
              </p>
          </el-card>
        </div>
      </el-col>
      <el-col :span="7">
        <Info></Info>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Info from './Info'
export default {
  data () {
    return {
      activeIndex: '1',
      articles: [],
      userId: 4
    }
  },
  components: { Info },
  created () {
    this.getArticleList()
  },
  methods: {
    clickTitle (articleId) {
      this.$router.push({ name: 'Article', params: { articleId: articleId } })
    },
    async getArticleList () {
      const { data: res } = await this.$http.get(`blog/${this.userId}/article`)
      this.articles = res.data.results
    },
    handleSelect () {
    }
  }
}
</script>

<style lang="less" scoped>
  .selection_title {
    height: 60px;
    padding: 20px 0;
  }
  .title_left {
    float: left;
    width: 40%;
    height: 100%;
  }
  .title_right {
    float: right;
    width: 60%;
    height: 100%;
  }
  .left_item {
    float: left;
    margin-right: 20px;
    line-height: 60px;
  }
  .right_item {
    float: right;
    margin-left: 10px;
    font-size: 30px;
    line-height: 60px;
  }
  .el-menu-item {
    font-size: 20px;
  }
  .article {
    padding: 20px;
    margin-bottom: 24px;
    a {
      font-size: 1.6rem;
      font-weight: 400;
    }
    div {
      margin: 8px 0;
      .el-tag {
        margin-right: 10px;
      }
    }
  }
  .desc {
    color: #666666;
    font-size: 1rem;
    a {
      font-size: 1rem;
      margin-left: 10px;
      color: #409EFF;
    }
  }
  .operate_info {
    margin: 10px 0 20px 0;
    span {
      margin-right: 180px;
      i {
        margin-right: 10px;
      }
    }
  }

</style>
