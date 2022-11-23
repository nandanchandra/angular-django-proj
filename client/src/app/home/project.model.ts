export class Project {
  public title: string;
  public description: string;
  public imageUrl: string;

  constructor(title: string, description: string, imageUrl: string) {
    this.title = title;
    this.description = description;
    this.imageUrl = imageUrl;
  }
}
