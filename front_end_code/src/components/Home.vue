<template>
    <el-container class="home_container">
      <el-header height="84px" v-show="showHeader">
        <div>
          <span class="title">TJ's Blog</span>
        </div>
        <div>
            <el-input
              class="search_inp"
              placeholder="请输入内容"
              prefix-icon="el-icon-search"
              v-model="queryInfo.query"
              clearable>
            </el-input>
        </div>
        <div>
          <span class="menu_item" @click="toHome()">文章</span>
          <span class="menu_item" @click="toDoList()">todolist</span>
          <span class="menu_item">others</span>
          <span class="menu_item" @click="test()">others</span>
        </div>
      </el-header>
      <el-container>
        <el-main>
          <router-view></router-view>
        </el-main>
      </el-container>
    </el-container>
</template>

<script>
export default {
  data () {
    return {
      queryInfo: {
        query: ''
      },
      showHeader: true,
      opacityStyle: {
        opacity: 0
      }
    }
  },
  created () {
  },
  methods: {
    handleScroll () {
      const top = document.documentElement.scrollTop
      if (top > 130) {
        let opacity = top / 140
        opacity = opacity > 1 ? 1 : opacity
        this.opacityStyle = { opacity }
        this.showHeader = false
      } else {
        this.showHeader = true
      }
    },
    toDoList () {
      this.$router.push({ name: 'ToDoList', params: {} })
    },
    toHome () {
      this.$router.push({ name: 'Home', params: {} })
    }
  },
  mounted () {
    window.addEventListener('scroll', this.handleScroll)
  },
  // 离开该页面需要移除这个监听的事件
  destroyed () {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style lang="less" scoped>
.home_container {
  height: 100%;
}
.el-header {
  position: fixed;
  width: 100%;
  background-color: #fff;
  display: flex;
  justify-content: space-between;
  padding: 0 50px;
  align-items: center;
  color: #7E8C8D;
  font-size: 30px;
  z-index: 11;
  > div {
    display: flex;
    align-items: center;
  }
  border: 1px solid #E6E6FA;
  box-shadow: 0 0 1px rgba(0,0,0,.25);
}
.el-main {
  margin-top: 96px;
  padding: 0 50px;
}
.title {
  color: #4F4F4F;
}
.menu_item {
  font-size: 24px;
  margin-right: 20px;
}

</style>
