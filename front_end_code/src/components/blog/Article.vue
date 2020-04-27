<template>
  <div style="padding-bottom: 80px;">
    <el-row :gutter="30">
      <el-col :span="17">
        <el-row>
          <div class="article_header">
            <div class="tags"><el-tag v-for="tag in article.tag_list" :type="tag.type" size="medium" :key="tag.id" effect="dark">{{tag.content}}</el-tag></div>
            <p class="title">{{article.title}}</p>
            <p class="operate_info">
              <span class="left_item">By / {{article.author_name}}</span>
              <span class="left_item">{{article.create_time | dateFormat}}</span>
              <span class="right_item"><i class="el-icon-view"></i>{{article.view}}</span>
              <span class="right_item"><i class="el-icon-star-on"></i>{{article.like}}</span>
            </p>
          </div>
        </el-row>
        <el-row>
          <div class="article_content">
          {{article.content}}
          </div>
        </el-row>
        <el-row class="comment">
          <div class="gt_meta">
            <span class="left_item">{{total}} 条评论</span>
            <span class="right_item">
              <el-dropdown trigger="click">
                <span class="el-dropdown-link">
                  未登录用户<i class="el-icon-arrow-down el-icon--right"></i>
                </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item icon="el-icon-plus">github登录</el-dropdown-item>
                  <el-dropdown-item icon="el-icon-circle-plus">QQ登录</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </span>
          </div>
        </el-row>
        <el-row :gutter="10">
          <el-col :span="2">
            <img src="../../assets/logo.png" alt="" width="48" height="48">
          </el-col>
          <el-col :span="22">
            <el-row>
              <el-input
                type="textarea"
                :autosize="{ minRows: 3, maxRows: 3}"
                placeholder="说点什么..."
                v-model="commentText"
                maxlength="64"
                show-word-limit
                resize="none"
                ref="input">
              </el-input>
            </el-row>
            <el-row>
              <el-alert
                title="注意：不得违反国家法律法规！"
                type="warning"
                show-icon
                :closable="false">
              </el-alert>
              <el-button type="primary" class="cmt_btn" @click="setInitialComment()">发布</el-button>
            </el-row>
          </el-col>
        </el-row>
        <!--已评论模块-->
        <el-row :gutter="10" class="commented" v-for="item in commented" :key="item.id">
          <el-col :span="2">
            <img :src="item.commentator_avatar" alt="" width="48" height="48">
          </el-col>
          <el-col :span="22" class="commented_box">
            <el-row>
              <el-row class="comment_msg">
                <span class="left_item username">{{item.username}}</span>
                <span class="left_item comment_at">发布于 {{item.comment_at}} 之前</span>
                <span class="right_item">
                  <a href="" v-on:click.prevent @click="setFollowUpCommitDisplay(item.id)"><i class="el-icon-s-comment"></i></a>
                </span>
              </el-row>
              <el-row>
                <p class="commented_content">{{item.content}}</p>
              </el-row>
            </el-row>
            <el-row :gutter="10" v-for="child in item.children" :key="child.id">
              <el-col :span="2">
                <img :src="child.avatar" alt="" width="36" height="36" style="margin:10px 0">
              </el-col>
              <el-col :span="22" class="commented_box">
                <el-row>
                  <el-row class="comment_msg">
                    <span class="left_item username">{{child.username}}</span>
                    <span class="left_item comment_at">发布于 {{child.comment_at}} 之前</span>
                  </el-row>
                  <el-row>
                    <p class="commented_content">{{child.content}}</p>
                  </el-row>
                </el-row>
              </el-col>
            </el-row>
            <el-row :id="item.id"  :style="{'display': item.replyDisplay}">
              <el-col :span="20">
                <el-input v-model="followUpCommentText"></el-input>
              </el-col>
              <el-col :span="4">
                <el-button type="primary" @click="setFollowUpCommit(item.id)" style="float: right">回复</el-button>
              </el-col>
            </el-row>
          </el-col>
        </el-row>

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
      articleId: null,
      userId: 4,
      article: {},
      commented: [],
      commentText: '',
      followUpCommentText: '',
      total: 0
    }
  },
  components: { Info },
  created () {
    this.articleId = this.$route.params.articleId
    this.getArticleDetail()
    this.getArticleComment()
  },
  methods: {
    async getArticleDetail () {
      const { data: res } = await this.$http.get(`blog/${this.userId}/article`, {
        articleId: this.articleId
      })
      if (res.data.meta.status !== 200) {
        return this.$message.error('获取article失败！')
      }
      this.article = res.data.results[0]
    },
    async getArticleComment () {
      const { data: res } = await this.$http.get(`blog/article/${this.articleId}/comment`)
      this.commented = res.data.results
      var that = this
      this.commented.forEach((item) => {
        const o = new Date(item.create_time)
        const n = new Date()
        const cha = n.getTime() - o.getTime()
        item.comment_at = that.timeFormat_(cha)
        item.children.forEach((etem) => {
          const o = new Date(etem.create_time)
          const n = new Date()
          const cha = n.getTime() - o.getTime()
          etem.comment_at = that.timeFormat_(cha)
        })
      })
      this.total = res.data.total
    },
    setFollowUpCommitDisplay (initialCommentId) {
      this.commented.forEach((item) => {
        if (item.id === initialCommentId) {
          item.replyDisplay = 'block'
        }
      })
    },
    async setInitialComment () {
      const { data: res } = await this.$http.post(`blog/article/${this.articleId}/comment`, {
        content: this.commentText,
        commentator: this.userId
      })
      if (res.data.meta.status !== 200) {
        return this.$message.error('评论失败！')
      }
      this.$message.success('评论成功！')
      this.commentText = ''
      this.getArticleComment()
    },
    async setFollowUpCommit (initialCommentId) {
      const { data: res } = await this.$http.post(`blog/article/${this.articleId}/reply`, {
        commentator: this.userId,
        initialcomment: initialCommentId,
        content: this.followUpCommentText
      })
      if (res.data.meta.status !== 200) {
        return this.$message.error('回复失败！')
      }
      this.$message.success('回复成功！')
      this.followUpCommentText = ''
      this.getArticleComment()
    },
    timeFormat_ (cha) {
      var days = Math.floor(cha / (24 * 3600 * 1000))
      if (days > 0) return days + '天'
      const leave1 = cha % (24 * 3600 * 1000)
      const hours = Math.floor(leave1 / (3600 * 1000))
      if (hours > 0) return hours + '小时'
      const leave2 = leave1 % (3600 * 1000)
      const minutes = Math.floor(leave2 / (60 * 1000))
      if (minutes > 0) return minutes + '分钟'
      const leave3 = leave2 % (60 * 1000)
      const seconds = Math.round(leave3 / 1000)
      return seconds + '秒'
    }
  }
}
</script>

<style lang="less" scoped>
  .article_header {
    padding: 20px 0 10px 0;
  }
  .tags .el-tag{
    margin-right: 15px;
  }
  .title {
    margin-top: 28px;
    font-size: 36px;
    line-height: 42px;
    font-weight: 500;
    color: #333;
    margin-bottom: 23px;
  }
  .operate_info {
    width: 100%;
    color: #878d99;
    font-size: 16px;
    font-weight: 400;
    vertical-align: baseline;
  }
  .left_item {
    float: left;
    margin-right: 30px;
  }
  .right_item {
    float: right;
    margin-left: 30px;
    i {
      padding-right: 10px;
    }
  }

  .article_content {
    width: 100%;
    margin: 40px 0;
  }
  .comment {
    height: 40px;
    margin: 20px 0;
    border-bottom: 1px solid lightgrey;
  }
  .el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
    font-size: 18px;
  }
  .el-icon-arrow-down {
    font-size: 16px;
  }
  .demonstration {
    display: block;
    color: #8492a6;
    font-size: 14px;
    margin-bottom: 20px;
  }
  .el-alert {
    float: left;
    margin-top: 20px;
    width: 80%;
  }
  .cmt_btn {
    margin-top: 20px;
    float: right;
  }
  .commented {
    margin-top: 50px;
  }
  .commented_box {
    background-color: #F9F9F9;
    padding: 12px 16px !important;
  }
  .username {
    font-size: 14px;
    font-weight: 500;
    color: #6190e8;
    text-decoration: none;
  }
  .comment_at {
    font-size: 14px;
    color: #a1a1a1;
    text-decoration: none;
  }
  .commented_content {
    font-size: 17px;
    margin: 15px 0;
    color: #333;
    word-wrap: break-word;
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol";
  }
</style>
