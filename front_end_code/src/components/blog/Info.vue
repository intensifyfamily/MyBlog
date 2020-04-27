<template>
  <div>
    <el-card>
      <img src="../../assets/images/info_top.jpg" alt="" width="100%" height="145px">
      <img class="avatar" :src="userInfo.avatar" alt="" width="100px" height="100px">
      <p class="name user_text">{{userInfo.username}}</p>
      <p class="des user_text">{{userInfo.motto}}</p>
      <a class="github" :href="userInfo.github"><img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=839120971,3274150665&fm=26&gp=0.jpg" alt="" width="80px" height="80px"></a>
      <el-divider></el-divider>
    </el-card>
  </div>
</template>

<script>
export default {
  data () {
    return {
      userInfo: {},
      userId: 4
    }
  },
  created () {
    this.getUserInfo()
  },
  methods: {
    async getUserInfo () {
      const { data: res } = await this.$http.get(`user/${this.userId}`)
      this.userInfo = res.data.results
    }
  }
}
</script>

<style lang="less" scoped>
    .avatar {
    position: relative;
    left: 50%;
    transform: translate(-50%, -50%);
    border-radius: 50%;
    border: 10px solid #E6E6FA;
  }
  .user_text {
    width: 100%;
    text-align: center;
  }
  .name {
    margin-top: -30px;
    font-size: 32px;
    color: #333;
    line-height: 30px;
    font-weight: 700;
  }
  .des {
    margin: 30px 0;
    font-size: 20px;
    color: #878d99;
    line-height: 30px;
    font-weight: 100;
  }
  .github {
    position: relative;
    left: 50%;
    transform: translate(-50%, 0);
    img {
      transform: translate(-50%, 0);
    }
  }
  .el-divider {
    width: 90%;
    margin-top: 20px;
    margin-left: 5%;
  }
</style>
