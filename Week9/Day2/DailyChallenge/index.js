class Video{
   constructor(title, uploader, time){
      this.title = title;
      this.uploader = uploader;
      this.time = time;
   }
   watch(){
      console.log(`${this.uploader} watched all ${this.time}}s of ${this.title}`)
   }
};

const video1 = new Video("JavaScript Basics", "JohnDoe123", 120);
video1.watch();
const video2 = new Video("React Tutorial", "JaneSmith456", 180);
video2.watch();

const videoData = [
   { title: "CSS Animations", uploader: "MikeJohnson789", time: 150 },
   { title: "Node.js Crash Course", uploader: "SarahBrown321", time: 240 },
   { title: "Python for Beginners", uploader: "DavidLee567", time: 200 },
   { title: "Vue.js Advanced Techniques", uploader: "EmilyDavis654", time: 210 },
   { title: "HTML5 Canvas Tutorial", uploader: "ChrisClark890", time: 180 }
 ];
 const videos = videoData.map(data => new Video(data.title, data.uploader, data.time));
 videos.forEach(video => video.watch());